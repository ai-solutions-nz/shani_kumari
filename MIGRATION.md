# Shani Kumari Website Migration

React + Vite site for Shani Kumari, Arizto Real Estate. This branch is a migration draft, not an approved production release.

## Run locally

```bash
npm install
npm run dev
npm run build
```

## Deploy to Netlify

Connect this GitHub repository to Netlify. Build command: `npm run build`, publish directory: `dist`. Do not move the domain from WordPress until content, form delivery, SEO, and QA are approved.

## Pages

Home, About, Listings, Sold, Testimonials, Videos, Appraisal/Contact, Thank You. Shared layout and navigation in `src/main.jsx`. Property records in `src/data/properties.js` and video metadata in `src/data/videos.js`.

## Content and launch blockers

- Migrate approved Shani portraits, original logo, brand elements, and real property photography.
- Import and verify live and sold listings, addresses, descriptions, property details, and sold credits.
- Migrate approved testimonials and property/video embeds. No fictional reviews or sales appear in this draft.
- Confirm biography copy, phone, email and all published agency / marketing claims with Shani.
- **Netlify Forms**: React-rendered forms require a detectable static HTML form at build time or another supported form provider. Implement static form detection and verify submission and email notifications before accepting enquiries.
- Add privacy policy, legal disclaimers, analytics, SEO metadata, canonical URLs, redirects from existing WordPress slugs, sitemap, social sharing images, accessibility checks.
- Test build, mobile devices, property links and all submission routes before merge and DNS cutover.

Based on supplied project material; original WordPress export has not been obtained. Keep WordPress live until the replacement is approved.
