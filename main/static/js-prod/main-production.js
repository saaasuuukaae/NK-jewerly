/******/ (function() { // webpackBootstrap
var __webpack_exports__ = {};
var LLImages = document.querySelectorAll("img[data-lazy-src]");
var LLCImages = document.querySelectorAll("*[data-lazy-css]");
var LLObserverOptions = {
  threshold: 1,
  rootMargin: "0px 0px 260px 0px"
};

var preLoadImage = function preLoadImage(obj) {
  var src = obj.getAttribute('data-lazy-src');

  if (!src) {
    return 0;
  } else {
    obj.src = src;
    obj.classList.add('image-loaded');
  }
};

var LLCallback = function LLCallback(entries, _LLObserver) {
  entries.forEach(function (entry) {
    if (!entry.isIntersecting) {
      return 0;
    } else {
      preLoadImage(entry.target);

      _LLObserver.unobserve(entry.target);
    }
  });
};

var LLObserver = new IntersectionObserver(LLCallback, LLObserverOptions);
LLImages.forEach(function (img) {
  LLObserver.observe(img);
});
/* ====================== header fadeIn ====================== */

var header = document.querySelector('.header');
var intro = document.querySelector('section#intro');
var sOOptions = {
  rootMargin: '100px 0px 0px 0px'
};

var sO = function sO(entries, _sO) {
  entries.forEach(function (entry) {
    if (!entry.isIntersecting) {
      header.classList.add('nav-scrolled');
    } else {
      header.classList.remove('nav-scrolled');
    }
  });
};

var sectionObserver = new IntersectionObserver(sO, sOOptions);
sectionObserver.observe(intro);
/* ====================== Lazy images gallery with css background ====================== */

var LLCObserverOptions = {
  threshold: [0, 0.25, 0.5, 0.75, 1] // rootMargin: "0px 0px 260px 0px"

};

var preLoadImageCSS = function preLoadImageCSS(obj) {
  var src = obj.getAttribute('data-lazy-css');

  if (!src) {
    return 0;
  } else {
    obj.style.backgroundImage = "url(\"".concat(src, "\")");
    obj.style.backgroundSize = 'cover';
    obj.removeAttribute('data-lazy-css');
    obj.classList.add('image-loaded');
  }
};

var LLCCallback = function LLCCallback(entries, _LLObserver) {
  entries.forEach(function (entry) {
    if (!entry.isIntersecting) {
      return 0;
    } else {
      preLoadImageCSS(entry.target);

      _LLObserver.unobserve(entry.target);
    }
  });
};

var LLCObserver = new IntersectionObserver(LLCCallback, LLCObserverOptions);
LLCImages.forEach(function (img) {
  LLCObserver.observe(img);
});
/******/ })()
;
//# sourceMappingURL=main-production.js.map