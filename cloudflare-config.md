# Cloudflare Configuration for IntentSim.org

## DNS Configuration

1. **Log in to your Cloudflare account**
2. **Select the intentsim.org domain**
3. **Navigate to the DNS section**

### Required DNS Records for GitHub Pages

Add the following A records to point to GitHub Pages servers:

| Type | Name | Content | Proxy Status |
|------|------|---------|-------------|
| A | @ | 185.199.108.153 | Proxied ☁️ |
| A | @ | 185.199.109.153 | Proxied ☁️ |
| A | @ | 185.199.110.153 | Proxied ☁️ |
| A | @ | 185.199.111.153 | Proxied ☁️ |
| CNAME | www | thevoidintent.github.io | Proxied ☁️ |

### DNS Configuration Screenshot:
![Example of properly configured Cloudflare DNS](https://developers.cloudflare.com/assets/static/57c13025684c5900502fac3b5cca476a/7e8ca/cf-dns-01.png)

## SSL/TLS Configuration

1. **Navigate to the SSL/TLS section**
2. **Configure the following settings:**

### Overview Tab
- Set SSL/TLS encryption mode to **Full (strict)**

### Edge Certificates Tab
- Enable **Always Use HTTPS**
- Enable **Automatic HTTPS Rewrites**

### Custom Hostnames Tab (Leave default)

## Page Rules (Optional but Recommended)

Create a page rule to force HTTPS:

1. Go to **Rules** > **Page Rules**
2. Click **Create Page Rule**
3. Enter `http://intentsim.org/*` as the URL pattern
4. Add the setting: **Always Use HTTPS**
5. Click **Save and Deploy**

## Optimizing Performance

For best performance of your IntentSim site:

1. **Navigate to Speed > Optimization**
2. Enable:
   - Auto Minify (HTML, CSS, JavaScript)
   - Brotli compression
   - Early Hints
   - Rocket Loader

## Caching Configuration

1. **Go to Caching > Configuration**
2. Set **Browser Cache TTL** to a reasonable value (e.g., 4 hours)
3. Under **Caching Rules**, consider adding a rule for static assets with a longer TTL

## Security Settings

1. **Go to Security > Settings**
2. Set Security Level to **Medium**
3. Enable Bot Fight Mode if needed

## Troubleshooting Common Issues

### DNS Not Propagating
- Wait at least 24 hours for complete propagation
- Use [DNS Checker](https://dnschecker.org) to verify records from different locations

### GitHub Pages Shows "DNS Check in Progress"
- This is normal while DNS propagates
- Check that your A records match exactly the GitHub Pages IP addresses
- Make sure the custom domain in GitHub Pages settings matches exactly your domain name

### HTTPS Not Working
- Ensure SSL/TLS is set to Full (strict)
- Verify that "Always Use HTTPS" is enabled
- Check that all Cloudflare proxies are enabled (orange cloud icon)

### Site Loads but Assets Don't
- Check if any assets are being blocked by Cloudflare security settings
- Review the browser console for any errors
- Verify path references in your HTML/CSS

Need help? Feel free to reach out for assistance with your Cloudflare configuration.
