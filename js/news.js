const spiderNews = new Splide('#splideNews',{
    type: 'loop',
    pagination: false,
    perPage: 2,
    perMove: 1,
    height: 400,
    width: 656,
    gap: 24,
    autoplay: true,
    arrows: boolean = false,
    padding: 10,
    breakpoints: {
        1320: {
            width: 856,
            padding: 0,
            focus: 'center',
            perPage: 3,
        },
        903: {
            width: 636, 
            perPage: 2,
            focus: 1,
        },
        659: { width: 306, perPage:1},
        600: { width: 306, perPage:1},
        550: { width: 306, perPage:1},
        500: { width: 306, perPage:1},
        450: { width: 306, perPage:1},
        400: { width: 306, perPage:1},
        350: { width: 306, perPage:1},
        300: { width: 306, perPage:1},
    },
});

spiderNews.mount();
