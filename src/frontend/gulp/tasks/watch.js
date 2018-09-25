const gulp = require('gulp'),
  livereload = require('gulp-livereload'),
  config = require('../config');


gulp.task('watch', gulp.series(function(done) {
  // Start livereload server first, so compile actions are also caught.
  // Dynamically look for all tasks ending in :watch, like sass:watch
  livereload.listen(config.livereload_options);
  const watchTasks = Object.keys(gulp.tasks).filter(name => name.endsWith(':watch'));
  return gulp.series(gulp.parallel(watchTasks), done);
}));
