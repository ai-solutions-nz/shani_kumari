# Shani Kumari — Website design and motion system

## Objective
Build a premium, approachable, trust-led Papamoa/Tauranga real estate website that is measurably better than the WordPress baseline. Use authentic Shani images, verified sold-property records and client feedback; never fabricate claims, reviews, prices or results.

## Visual principles
- Editorial, calm, warm-white canvas with forest/sage greens and restrained brass/tan accents. Respect supplied logo and brand assets.
- Distinctive large serif headlines paired with legible sans-serif body text; strong visual hierarchy and generous whitespace.
- Portrait-led hero with one clear promise and primary **Request a free appraisal** action; secondary **Explore sold homes**.
- Mobile first: tap targets >=44px, readable contrast, no horizontal overflow, stable image aspect ratios.
- Build original compositions rather than copying proprietary templates or screenshots.

## Components and source libraries
- **Embla Carousel** (https://github.com/davidjerleke/embla-carousel): preferred swipeable sold-property carousel. Inspect licence and current version before installation; keyboard controls, accessible buttons, pagination and reduced-motion support.
- **Motion for React** (https://github.com/motiondivision/motion): selective section and image reveals, no movement that delays reading or interaction.
- **shadcn/ui** (https://github.com/shadcn-ui/ui): selectively adopt accessible patterns, not a full design-system transplant.
- **GSAP** (https://github.com/greensock/GSAP): only for a demonstrated need not covered by CSS or Motion; verify licensing and bundle cost.

## Motion constraints
- Motion is subordinate to trust and comprehension. Keep entrance animation around 200–450ms; avoid scroll-jacking, parallax on mobile, distracting looping effects and layout shifts.
- Respect `prefers-reduced-motion: reduce`; make all content usable with JavaScript animation disabled.
- Prioritize smooth scrolling only where native behavior suffices; defer noncritical animation bundles.

## Page structure
1. Home: agent identity, geographic relevance, real portrait, clear appraisal CTA, value proposition, recent sold carousel, proof/testimonials, concise process, contact.
2. About: authentic biography and approved imagery; no unverifiable qualifications.
3. Listings: current verified properties only, dated status or direct source links.
4. Sold: approved property images, verified addresses and sale details when permitted.
5. Testimonials: preserve exact sourced text and attribution.
6. Videos: working, permissioned embeds with accessible titles.
7. Appraisal/contact: validated form, privacy explanation, actual tested delivery, phone and email fallback.
8. Legal: real approved policies and agency disclosures.

## WordPress-to-Bolt process
- GitHub repo: `ai-solutions-nz/shani_kumari`; branch: `website/react-vite-migration`. Never write directly to main.
- Google Drive asset backup: https://drive.google.com/drive/folders/1faVs2DFambDmjdYrtxkyE8KR4j_e4aUH.
- First ensure all original image binaries exist in `public/images`; do not replace working WordPress URLs with nonexistent local files.
- Import the **latest branch** into Bolt.new; verify branch/project identity and round-trip GitHub sync.
- Bolt hosting is the intended deployment platform; remove Netlify Forms integration and implement tested Bolt-compatible delivery.
- WordPress stays live until owner approves a fully tested preview and domain cutover.

## Quality gates
- Build passes; every image loads and is optimized; no broken routes; keyboard and touch interaction work.
- Lighthouse targets >=90 performance/accessibility/SEO on representative mobile pages where feasible; record actual scores and exceptions.
- Appraisal submission confirmed delivered to Shani; privacy and anti-spam checks.
- Verify mobile 360px, tablet and desktop; no motion-induced CLS.
- Preserve URLs/SEO metadata, implement redirects and document rollback.
- Never claim preview, deployment or tests without actual evidence.
