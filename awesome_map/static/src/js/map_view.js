odoo.define('awesome_map.MapView', function (require) {
"use strict";

var AbstractView = require('web.AbstractView');
var viewRegistry = require('web.view_registry');

var MapView = AbstractView.extend({});
console.log('test ABC');
viewRegistry.add('map', MapView);

});
