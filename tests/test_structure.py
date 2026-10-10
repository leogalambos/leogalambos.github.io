"""Dependency-free source and route tests for the personal GitHub Pages site."""
from pathlib import Path
import re
import unittest
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / 'docs'


class SiteStructureTests(unittest.TestCase):
    def test_pages_exist(self):
        pages = ('index.md', 'about.md', 'contact.md', 'work/index.md',
                 'work/jai.md', 'work/radixor.md', 'work/egothor-v4.md',
                 'work/zeroecho.md', 'work/conflux.md', 'work/methodatlas.md',
                 'work/heritage.md')
        for relative in pages:
            with self.subTest(page=relative):
                self.assertTrue((DOCS / relative).is_file())

    def test_publications_are_with_projects(self):
        all_pages = [p.relative_to(DOCS).as_posix() for p in DOCS.rglob('*.md')]
        self.assertNotIn('publications.md', all_pages)
        self.assertNotIn('research.md', all_pages)
        rad = (DOCS / 'work/radixor.md').read_text()
        self.assertEqual(len(re.findall(r'class="paper-row"', rad)), 9)
        self.assertIn('Research & publications', rad)
        self.assertIn('Research & publications', (DOCS / 'work/jai.md').read_text())

    def test_commercial_attribution_is_neutral(self):
        html = '\n'.join(p.read_text() for p in DOCS.rglob('*.md'))
        self.assertNotIn(''.join(('Ac', 'cen', 'ture')), html)
        self.assertNotIn('github.com/' + ''.join(('Ac', 'cen', 'ture')) + '/', html)
        self.assertIn('MethodAtlas', html)
        self.assertIn('adapted for commercial use', html)
        self.assertTrue((DOCS / 'work/methodatlas.md').exists())
        self.assertNotIn('MethodAtlas', (DOCS / 'work/heritage.md').read_text())

    @staticmethod
    def target_dir(page: Path):
        relative = page.relative_to(DOCS)
        return relative.parent / (relative.stem if relative.stem != 'index' else '')

    @staticmethod
    def resolved_link(source: Path, url: str):
        path = str(source) + '/' + url.split('#')[0].split('?')[0]
        stack = []
        for section in path.split('/'):
            if section == '..':
                if stack:
                    stack.pop()
            elif section not in ('', '.'):
                stack.append(section)
        return '/'.join(stack)

    def test_local_html_links_point_to_real_routes(self):
        destinations = {str(self.target_dir(p)).strip('.') for p in DOCS.rglob('*.md')}
        destinations.add('')
        for page in DOCS.rglob('*.md'):
            for url in re.findall(r'href="([^"]+)"', page.read_text()):
                if url.startswith(('http:', 'https:', '#', 'mailto:')):
                    continue
                dest = self.resolved_link(self.target_dir(page), url)
                with self.subTest(source=page.name, url=url, route=dest):
                    self.assertIn(dest, destinations)

    def test_markdown_relative_links_use_source_md_paths(self):
        # MkDocs rewrites links pointing at .md sources, not guessed deployed URL.
        for page in DOCS.rglob('*.md'):
            for url in re.findall(r'(?<!!)\[[^\]]+\]\(([^)]+)\)', page.read_text()):
                url = url.split(' ', 1)[0].split('#', 1)[0]
                if not url or url.startswith(('http:', 'https:', '#', 'mailto:')):
                    continue
                target = (page.parent / url).resolve()
                with self.subTest(source=str(page.relative_to(DOCS)), url=url):
                    self.assertEqual(target.suffix, '.md')
                    self.assertTrue(target.is_file())

    def test_image_references(self):
        for page in DOCS.rglob('*.md'):
            published = self.target_dir(page)
            for asset in re.findall(r'\bsrc="([^"#]+)"', page.read_text()):
                if asset.startswith(('http:', 'https:', '/')):
                    continue
                path = self.resolved_link(published, asset)
                with self.subTest(source=page.name, asset=asset):
                    self.assertTrue((DOCS / path).is_file())

    def test_hero_asset_is_clean_and_self_contained(self):
        img = DOCS / 'assets/img/hero-landscape.webp'
        self.assertTrue(img.is_file())
        self.assertGreater(img.stat().st_size, 10_000)
        page = (DOCS / 'index.md').read_text()
        self.assertIn('lg-hero', page)
        self.assertNotIn('art-globe.webp', page)
        css = (DOCS / 'assets/css/landing.css').read_text()
        self.assertIn('hero-landscape.webp', css)
        self.assertNotIn('https://', css)

    def test_bundled_project_illustrations(self):
        for name in ('jai', 'egothor', 'radixor', 'zeroecho', 'conflux', 'methodatlas'):
            self.assertTrue((DOCS / f'assets/img/art-{name}.webp').exists())
        for name in ('brandmark', 'favicon', 'art-network'):
            ElementTree.parse(DOCS / f'assets/img/{name}.svg')

    def test_project_navigation_on_homepage(self):
        t = (DOCS / 'index.md').read_text()
        self.assertEqual(t.count('class="lg-card"'), 6)
        self.assertIn('href="contact/"', t)
        self.assertIn('href="about/"', t)
        self.assertIn('href="work/"', t)

    def test_single_row_real_material_header(self):
        import jinja2
        import yaml
        conf = yaml.safe_load((ROOT / 'mkdocs.yml').read_text())
        self.assertEqual(conf['theme']['custom_dir'], 'overrides')
        self.assertNotIn('navigation.tabs', conf['theme']['features'])
        self.assertNotIn('navigation.tabs.sticky', conf['theme']['features'])
        self.assertIn('assets/css/header.css', conf['extra_css'])
        template = (ROOT / 'overrides/partials/header.html').read_text()
        jinja2.Environment().parse(template)
        self.assertIn('class="md-header', template)
        self.assertIn('data-md-component="header"', template)
        self.assertIn('for="__drawer"', template)
        self.assertIn('partials/search.html', template)
        self.assertIn('partials/palette.html', template)
        self.assertIn('partials/javascripts/palette.html', template)
        self.assertIn('LEO GALAMBOS', template)
        self.assertNotIn('RNDr.', template)
        self.assertNotIn('Ph.D.', template)
        homepage = (DOCS / 'index.md').read_text()
        self.assertNotIn('RNDr.', homepage)
        self.assertNotIn('Ph.D.', homepage)
        self.assertIn('RNDr. Leo Galambos, Ph.D.', (DOCS / 'about.md').read_text())
        self.assertNotIn('::after{content:', (DOCS / 'assets/css/landing.css').read_text())

    def test_header_renders_without_page_for_404(self):
        # MkDocs Material renders 404.html with page=None; the header must be safe.
        from types import SimpleNamespace
        from jinja2 import ChoiceLoader, DictLoader, Environment, FileSystemLoader, StrictUndefined

        partials = {
            '.icons/material/menu.svg': '<svg id="menu"></svg>',
            '.icons/material/magnify.svg': '<svg id="search-icon"></svg>',
            '.icons/fontawesome/brands/github.svg': '<svg id="github"></svg>',
            'partials/search.html': '<section id="native-search"></section>',
            'partials/palette.html': '<section id="native-palette"></section>',
            'partials/javascripts/palette.html': '<section id="palette-scripts"></section>',
        }
        env = Environment(
            loader=ChoiceLoader([FileSystemLoader(ROOT / 'overrides'), DictLoader(partials)]),
            undefined=StrictUndefined,
            autoescape=True,
        )
        env.filters['url'] = lambda value: '/' + value.lstrip('/')
        template = env.get_template('partials/header.html')
        config = SimpleNamespace(
            theme=SimpleNamespace(icon=SimpleNamespace(menu=None, search=None), palette=[{'scheme':'default'}]),
            plugins={'material/search': SimpleNamespace(config=SimpleNamespace(enabled=True))},
        )
        nav = SimpleNamespace(homepage=SimpleNamespace(url=''))
        scenarios = (
            ('404', {'page': None}, None),
            ('missing page context', {}, None),
            ('home', {'page': SimpleNamespace(url='', is_homepage=True)}, 'Home'),
            ('project', {'page': SimpleNamespace(url='work/jai/', is_homepage=False)}, 'Projects'),
            ('profile', {'page': SimpleNamespace(url='about/', is_homepage=False)}, 'Profile'),
            ('contact', {'page': SimpleNamespace(url='contact/', is_homepage=False)}, 'Contact'),
        )
        for name, page_context, active in scenarios:
            with self.subTest(context=name):
                markup = template.render(config=config, nav=nav, **page_context)
                self.assertIn('LEO GALAMBOS', markup)
                self.assertIn('id="native-search"', markup)
                self.assertIn('id="native-palette"', markup)
                self.assertIn('href="/contact/"', markup)
                if active is None:
                    self.assertNotIn('is-active', markup)
                elif active == 'Projects':
                    self.assertIn('lg-site-nav-group is-active', markup)
                else:
                    self.assertIn('is-active', markup)

    def test_valid_configuration(self):
        import yaml
        config = yaml.safe_load((ROOT / 'mkdocs.yml').read_text())
        self.assertEqual(config['site_url'], 'https://leogalambos.github.io/')
        self.assertEqual(config['theme']['name'], 'material')
        self.assertIn('assets/css/landing.css', config['extra_css'])
        self.assertIn({'MethodAtlas': 'work/methodatlas.md'}, config['nav'][1]['Projects'])
        self.assertIn({'Contact': 'contact.md'}, config['nav'])

if __name__ == '__main__':
    unittest.main()
