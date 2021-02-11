const $ = window.$;
$('div#update_header').click(function () {
  if ($('header').text() !== 'New Header!!!') {
    $('header').text('New Header!!!');
  } else {
    $('header').text('First HTML page');
  }
});
