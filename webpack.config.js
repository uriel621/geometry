var webpack = require("webpack");
var path = require('path');

module.exports = {
	entry: {
		app: "./src/index.js"
	},
	output: {
		filename:"static/bundle.js",
	},

	module: {
		loaders: [
			{
				test: /\.jsx?$/,
				exclude: /(node_modules|bower_components)/,
				loader: 'babel-loader',
				query:{
					presets:['react', 'es2015']
				}
			}
		]
	}
}
