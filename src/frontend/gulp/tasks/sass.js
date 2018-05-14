'use strict';

const gulp = require('gulp'),
  filesExist = require('files-exist'),
  plumber = require('gulp-plumber'),
  sass = require('gulp-sass'),
  sourcemaps = require('gulp-sourcemaps'),
  livereload = require('gulp-livereload'),
  postcss = require('gulp-postcss'),
  notify = require('gulp-notify'),
  size = require('gulp-size'),
  config = require('../config');

var NODE_ENV = process.env.NODE_ENV;


function handleErrors() {
  var args = Array.prototype.slice.call(arguments);

  // Alternative instead of default sass.logError
  // Send error to Mac notification center with gulp-notify:
  notify.onError({
    title: "Compile Error",
    message: "<%= error.message %>"
  }).apply(this, args);

  this.emit('end');
}


gulp.task('sass', function () {
  // Task to compile sass
  return gulp.src(filesExist(config.paths.sass_glob))
    .pipe(plumber({errorHandler: handleErrors}))
    .pipe(sourcemaps.init())
    .pipe(sass(config.sass_options))
    .pipe(postcss(config.postcss_plugins))
    .pipe(sourcemaps.write('.'))
    .pipe(size({showFiles: true}))
    .pipe(gulp.dest(config.paths.css))
    .pipe(livereload())
});


gulp.task('sass:watch', ['sass'], function () {
  // Watch and recompile on changes
  return gulp.watch(config.paths.sass_glob, ['sass'])
    .on('change', function (evt) {
      console.log('[watcher] File ' + evt.path.replace(/.*(?=sass)/, '') + ' was ' + evt.type + ', compiling...');
    });
});
