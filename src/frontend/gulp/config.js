'use strict';

const autoprefixer = require('autoprefixer'),
  mqpacker = require('css-mqpacker'),
  cssnano = require('cssnano');

const bootstrap = 'node_modules/bootstrap-sass/assets/javascripts/';
const vendor = './frontend/static/frontend/vendor/';

const NODE_ENV = process.env.NODE_ENV;

let postcss_plugins = [
    // All post-processing happens in one batch, no reparsing of CSS is done here.
    autoprefixer({
      browsers: [
        ">0.25%",
        "not ie 11",
        "not op_mini all"
      ],
      cascade: false
    }),
    mqpacker({sort: true})  // combine media queries
  ];

if(NODE_ENV === 'production') {
  postcss_plugins.push(cssnano());
}


module.exports = {
  paths: {
    sass: './frontend/sass/',
    sass_glob: './frontend/sass/**/*.scss',
    css: './frontend/static/frontend/css/',
    images: './frontend/static/frontend/images/',
    spriteInput: './frontend/static/frontend/images/sprites/*/*.png',
    vendor: vendor
  },

  copy_files: [
    {
      src: [
        'node_modules/jquery/dist/jquery.min.js'
      ],
      dest: vendor
    },
    {
      src: [
        bootstrap + 'bootstrap/collapse.js',
        bootstrap + 'bootstrap/transition.js'
      ],
      dest: vendor + "bootstrap/"
    }
  ],

  sass_options: {
    // See https://github.com/sass/node-sass
    outputStyle: NODE_ENV === 'production' ? 'compressed' : 'expanded',
    includePaths: [
      './frontend/sass-vendor/',
      './node_modules/bootstrap-sass/assets/stylesheets/',
    ],
    precision: 5
  },

  postcss_plugins: postcss_plugins,

  livereload_options: {
    host: '127.0.0.1'
  },

  mozjpeg_options: {
    quality: 80,
    progressive: true
  },

  pngquant_options: {
    quality: '40-100',
    verbose: true
  }
};
