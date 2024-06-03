const swiperNew = new Swiper('.swiper_news', {
    slidesPerView: 2,
    spaceBetween: 30,
    autoplay: {
        delay: 5000,
    },
    pagination: {
        el: '.swiper-pagination_news',
        clickable: true,
    },
});
