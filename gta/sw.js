// GTA: Giuseppe Taglia Alberi — Service Worker (Offline Cache & PWA)
const CACHE_NAME = 'gta-augusta-v1.0.2';
const STATIC_ASSETS = [
  './',
  './index.html',
  './manifest.webmanifest',
  './logo-gta.webp',
  './icon-32.png',
  './icon-180.png',
  './icon-192.png',
  './icon-512.png',
  './cover-art.webp',
  './og-preview.png',
  '../bundle/index-gta-v1.js?v=20260927-grounded-physics',
  '../bundle/index-DjewJEKc.css?v=20260927-grounded-physics',
  '../bundle/bead-BuU2NiVW.webp',
  '../bundle/button-cream-46cWyhPk.webp',
  '../bundle/button-orange-Blh8rKCL.webp',
  '../bundle/sans-bold-DrYefe97.woff',
  '../bundle/sans-medium-Bkgwalw7.woff',
  '../bundle/display-C9le1XGG.woff',
  '../bundle/hand-C0ee-cRK.woff',
  '../bundle/jump-gY1Z4E5y.wav',
  '../bundle/coin-pickup-d4kv-Dau.wav',
  '../bundle/switch-press-BRz_CuqN.wav',
  '../bundle/finish-bell-1vPK9VCS.wav'
];

self.addEventListener('install', (event) => {
  self.skipWaiting();
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll(STATIC_ASSETS).catch((err) => {
        console.warn('Some assets could not be cached immediately:', err);
      });
    })
  );
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) => {
      return Promise.all(
        keys.map((key) => {
          if (key !== CACHE_NAME) {
            return caches.delete(key);
          }
        })
      );
    }).then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (event) => {
  if (event.request.method !== 'GET') return;
  event.respondWith(
    caches.match(event.request).then((cached) => {
      if (cached) return cached;
      return fetch(event.request).then((response) => {
        if (!response || response.status !== 200 || response.type !== 'basic') {
          return response;
        }
        const toCache = response.clone();
        caches.open(CACHE_NAME).then((cache) => {
          cache.put(event.request, toCache);
        });
        return response;
      }).catch(() => {
        // Fallback to cached index.html for navigation
        if (event.request.mode === 'navigate') {
          return caches.match('./index.html');
        }
      });
    })
  );
});
