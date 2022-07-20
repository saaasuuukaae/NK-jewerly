const LLImages = document.querySelectorAll("img[data-lazy-src]")
const LLCImages = document.querySelectorAll("*[data-lazy-css]")


const LLObserverOptions = {
    threshold: 1,
    rootMargin: "0px 0px 260px 0px"
}

const preLoadImage = (obj) => {
    let src = obj.getAttribute('data-lazy-src');
    if (!src) {
        return 0;
    } else {
        obj.src = src
        obj.classList.add('image-loaded')
    }
}

const LLCallback = (entries, _LLObserver) => {

    entries.forEach(entry => {
        if (!entry.isIntersecting) {
            return 0;
        } else {
            preLoadImage(entry.target);
            _LLObserver.unobserve(entry.target)
        }
    })

}

const LLObserver = new IntersectionObserver(LLCallback, LLObserverOptions)

LLImages.forEach(
    img => {
        LLObserver.observe(img)
    }
)

/* ====================== header fadeIn ====================== */

const header = document.querySelector('.header');
const intro = document.querySelector('section#intro');
const sOOptions = {
    rootMargin: '0px 0px 0px 0px',
}

const sO = (entries, sO) => {
    entries.forEach(entry => {
        if (!entry.isIntersecting) {
            header.classList.add('nav-scrolled')
        } else {
            header.classList.remove('nav-scrolled')
        }
    })
}

const sectionObserver = new IntersectionObserver(
    sO, sOOptions
)

sectionObserver.observe(intro)

/* ====================== Lazy images gallery with css background ====================== */

const LLCObserverOptions = {
    threshold: [0, 0.25, 0.5, 0.75, 1],
    // rootMargin: "0px 0px 260px 0px"
}

const preLoadImageCSS = (obj) => {
    let src = obj.getAttribute('data-lazy-css');
    if (!src) {
        return 0;
    } else {
        obj.style.backgroundImage = `url("${src}")`
        obj.style.backgroundSize = 'cover'

        obj.removeAttribute('data-lazy-css')
        obj.classList.add('image-loaded')
    }
}

const LLCCallback = (entries, _LLObserver) => {

    entries.forEach(entry => {
        if (!entry.isIntersecting) {
            return 0;
        } else {
            preLoadImageCSS(entry.target);
            _LLObserver.unobserve(entry.target)
        }
    })

}

const LLCObserver = new IntersectionObserver(LLCCallback, LLCObserverOptions)

LLCImages.forEach(
    img => {
        LLCObserver.observe(img)
    }
)

