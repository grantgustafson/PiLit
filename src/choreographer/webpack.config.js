module.exports = {
    entry: "./static/choreo.js",
    output: {
        filename: "./static/bundle.js"
    },
    module: {
        loaders: [
            {
            test: /\.jsx?$/,
            exclude: /(node_modules|bower_components)/,
            loader: 'babel-loader',
            query: {
                presets: ['es2015']
            }
            }
        ]
    }
}
