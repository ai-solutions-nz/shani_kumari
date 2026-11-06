# Shani Kumari image migration manifest

Source: https://shanikumari.co.nz (WordPress media library).
Drive backup: https://drive.google.com/drive/folders/1faVs2DFambDmjdYrtxkyE8KR4j_e4aUH (23 original media files copied from existing Shani Drive assets).

## GitHub image import

The workflow at `.github/workflows/import-wordpress-images.yml` downloads 12 original WordPress image binaries to `public/images/` and commits them to `website/react-vite-migration`. It must be triggered from GitHub Actions and its result verified. This manifest is NOT evidence that binaries are already committed.

| Local image path | Original WordPress image URL |
| --- | --- |
| public/images/shani-kumari-green-logo.png | https://shanikumari.co.nz/wp-content/uploads/2025/05/Shani-Kumari-green-logo.png |
| public/images/shani-kumari-white-logo.png | https://shanikumari.co.nz/wp-content/uploads/2025/05/Shani-Kumari-White-logo.png |
| public/images/about-shani.png | https://shanikumari.co.nz/wp-content/uploads/2025/05/about-shani.png |
| public/images/mobile-hero.png | https://shanikumari.co.nz/wp-content/uploads/2025/05/mobile-hero.png |
| public/images/featured-1.png | https://shanikumari.co.nz/wp-content/uploads/2025/05/featured-1.png |
| public/images/feature-3.png | https://shanikumari.co.nz/wp-content/uploads/2025/05/feature-3.png |
| public/images/4-1.png | https://shanikumari.co.nz/wp-content/uploads/2025/06/4-1.png |
| public/images/8-1.png | https://shanikumari.co.nz/wp-content/uploads/2025/06/8-1.png |
| public/images/5-1.png | https://shanikumari.co.nz/wp-content/uploads/2025/06/5-1.png |
| public/images/7-1.png | https://shanikumari.co.nz/wp-content/uploads/2025/06/7-1.png |
| public/images/featured-ohauiti.png | https://shanikumari.co.nz/wp-content/uploads/2026/01/Copy-of-Untitled-Design-1.png |
| public/images/featured-courtney.png | https://shanikumari.co.nz/wp-content/uploads/2025/09/36-courtney.png |

## Before switching to local URLs

1. Run the import workflow on GitHub and confirm all 12 files exist and are valid images.
2. Replace WordPress URLs in `src/data/media.js` and `src/data/properties.js` with matching `/images/...` paths.
3. Run the Vite production build and test responsive layouts, images and links.
4. Keep the WordPress host active until the new site is verified.
