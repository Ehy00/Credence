/** @type {import('next').NextConfig} */
const nextConfig = {
  // Remove 'standalone' output for Vercel - it handles this automatically
  // output: 'standalone', // Only for Docker deployments
  experimental: {
    outputFileTracingIncludes: {
      '/': ['./data/**/*'],
    },
  },
};

export default nextConfig;

