var config = require('./webpack.config');

module.exports = Object.assign({}, config, {
    entry: [
        './static/js/index'
    ],
});
