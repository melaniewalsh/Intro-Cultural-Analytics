// Works like jQuery's $(document).ready.
// Supports IE8+. Courtesy of http://youmightnotneedjquery.com/
function ready(fn) {
  if (document.readyState != 'loading') {
    fn();
  } else if (document.addEventListener) {
    document.addEventListener('DOMContentLoaded', fn);
  } else {
    document.attachEvent('onreadystatechange', function() {
      if (document.readyState != 'loading')
        fn();
    });
  }
}

ready(function() {

  var website = window.location.hostname;

  var internalLinkRegex = new RegExp('^((((http:\\/\\/|https:\\/\\/)(www\\.)?)?'
                                     + website
                                     + ')|(localhost:\\d{4})|(\\/.*))(\\/.*)?$', '');

  var anchorEls = document.querySelectorAll('a.reference.external, a.binder-button, a.issues-button');
  var anchorElsLength = anchorEls.length;

  for (var i = 0; i < anchorElsLength; i++) {
    var anchorEl = anchorEls[i];
    var href = anchorEl.getAttribute('href');

    if (!internalLinkRegex.test(href)) {
      anchorEl.setAttribute('target', '_blank');
    }
  }
});
