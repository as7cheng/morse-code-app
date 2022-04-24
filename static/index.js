$(document).ready(function () {
    const curRoute = window.location.pathname.slice(1).split('/')[0];
    $(`#${curRoute}`).addClass('active');
})