# Shani Kumari — WordPress migration acceptance register

**Source:** https://shanikumari.co.nz/  
**Destination:** `ai-solutions-nz/shani_kumari`, branch `website/react-vite-migration`  
**Target editor/hosting:** Bolt.new / Bolt hosting, **not Netlify**.  
**Status:** IN PROGRESS — no production cutover authorized.

## Source inventory and evidence

| WordPress content / function | Destination | Status | Verification required |
| --- | --- | --- | --- |
| Homepage and introductory copy | `/` | Draft migrated | Compare live copy, media, calls to action |
| About Shani | `/about` | Draft migrated | Confirm biography and claims with Shani |
| Services | Home and About | Partially migrated | Compare all service inclusions and fees |
| Featured properties | `/listings` | Two records migrated | Confirm current status and permission to advertise |
| Recently sold gallery | `/sold` | Six image references migrated | Download binaries; verify properties and credits |
| Testimonials | `/testimonials` | Four published testimonials migrated | Confirm full attribution, exact text and permission |
| Videos | `/videos` | Three embeds referenced | Confirm playback and video ownership |
| Contact / appraisal | `/appraisal` | UI draft only | **Form cannot be assumed operational on Bolt hosting** |
| Terms and Conditions | `/terms-and-conditions` | WordPress link only | Preserve full source text; agency/legal review |
| Privacy Policy | `/privacy-policy` | WordPress link only | Preserve full source text; privacy review |
| REA / complaints | `/rea` | WordPress link only | Preserve official disclosure and process |
| WordPress blog posts | No equivalent yet | Not migrated | Inventory posts, decide migration/redirects |
| WordPress images and video | `public/images`, `public/video` | **Not committed** | Download, hash/validate and verify all files |
| SEO metadata, slugs, sitemap | Route metadata and redirects | Not verified | Crawl source and test redirects |
| Mobile accessibility/performance | All routes | Not verified | Build, keyboard, responsive and Lighthouse checks |

## Media transfer

- A separate Google Drive backup contains 23 copied media files: https://drive.google.com/drive/folders/1faVs2DFambDmjdYrtxkyE8KR4j_e4aUH.
- `IMAGE-MIGRATION.md` lists 12 WordPress images and `.github/workflows/import-wordpress-images.yml` contains a manual download workflow.
- **No image should be switched to a local URL until its binary exists in the GitHub repository.**
- Importing 12 files does not prove the complete WordPress media library is migrated. Compare source gallery, featured properties, original Shani Drive assets, and all page images.

## Source inconsistencies to resolve

- Homepage body displays `shani.kumari@arizto.co.nz`; migration data currently uses `shani.k@arizto.co.nz`. Source footer contains an apparent malformed address. **Obtain Shani's confirmation before enabling enquiry delivery.**
- Source homepage contains sales figures and experience statements that require approval; do not silently publish or extrapolate them.
- Featured property status may have changed since source capture; do not describe an old listing as currently for sale without verification.
- Source Terms and Conditions describe specific fees and agency obligations. Preserve exact text, do not paraphrase legal obligations, and request agency approval.

## Build and delivery verification

A local check of an older available migration ZIP could not install npm dependencies in offline mode (missing cached `lucide-react`); this is **not** a build test of the latest GitHub branch. Production build remains unverified.

- Confirm GitHub Actions `build.yml` passes on the migration branch.
- Import the correct repository into Bolt only after content and asset verification.
- Replace Netlify-specific form markup with a Bolt-compatible backend or trusted form provider; test receipt, validation, spam prevention and privacy notice.
- Review source versus destination on mobile and desktop.
- Preserve original site and rollback plan until approval.

## Next operator action

1. Trigger `Import WordPress images` workflow from GitHub Actions on `website/react-vite-migration`, verify the actual committed binaries.
2. Convert `src/data/media.js` and `src/data/properties.js` to local asset paths only after verification.
3. Complete missing legal, service, blog and SEO content inventory; obtain approval for legal copy and conflicting contact details.
4. Run build, link checks, form tests and a page-by-page comparison.
5. Present evidence and request separate approval before production cutover.
