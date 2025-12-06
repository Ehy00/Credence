/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'standalone',
  // Enable standalone output for Docker
  experimental: {
    outputFileTracingIncludes: {
      '/': ['./data/**/*'],
    },
  },
};

export default nextConfig;

