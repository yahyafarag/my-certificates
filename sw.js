const CACHE_NAME = 'yahya-eng-cache-v1';
const urlsToCache = [
  '/yahya-web-site/',
  '/yahya-web-site/index.html',
  '/yahya-web-site/index-ar.html',
  '/yahya-web-site/assets/css/style.css',
  '/yahya-web-site/assets/images/profile/yahya-profile.webp'
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        return cache.addAll(urlsToCache);
      })
  );
});

self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => {
        return response || fetch(event.request);
      })
  );
});
