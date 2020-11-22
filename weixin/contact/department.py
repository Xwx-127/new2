import pystache

print(pystache.render('Hello {{name}} {{#show}} ,i am {{call}} {{/show}}',
                      {'name':'world',
                       'call':'小祥哥',
                       'show':['a','b','c']}))




