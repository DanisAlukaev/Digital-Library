module.exports = {
    publicPath: '',
    configureWebpack: {
        module: {
            rules: [
                {
                    test: /\.worker\.js$/,
                    use: {loader: 'worker-loader'}
                }
            ]
        }
    }
};