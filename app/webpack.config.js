module.exports = {
    entry: "./components/Main.js",
    output: {
        filename: "../src/server/static/bundle.js"
    },
    module: {
        loaders: [
            {
            test: /\.jsx?$/,
            exclude: /(node_modules|bower_components)/,
            loader: 'babel-loader',
            query: {
                presets: ['react', 'es2015']
            }
            }
        ]
    }
}
