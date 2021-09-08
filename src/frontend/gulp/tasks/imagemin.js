const gulp = require("gulp"),
  webp = require('gulp-webp'),
  merge = require("merge-stream"),
  plumber = require("gulp-plumber"),
  imagemin = require("gulp-imagemin"),
  imageminPngquant = require("imagemin-pngquant"),
  imageminMozjpeg = require("imagemin-mozjpeg"),
  size = require("gulp-size"),
  config = require("../config");

function minifyImages() {
  const pngs = gulp
    .src(config.paths.images + "**/*.png")
    .pipe(plumber())
    .pipe(imagemin([imageminPngquant(config.pngquant_options)]))
    .pipe(size({ showFiles: true, showTotal: false }))
    .pipe(gulp.dest(config.paths.dist));

  const jpegs = gulp
    .src(config.paths.images + "**/*.{jpg,jpeg}")
    .pipe(plumber())
    .pipe(imagemin([imageminMozjpeg(config.mozjpeg_options)]))
    .pipe(size({ showFiles: true, showTotal: false }))
    .pipe(gulp.dest(config.paths.dist));

  const pngsToWebp = gulp
    .src(config.paths.images + "**/*.png")
    .pipe(plumber())
    .pipe(webp({lossless: true, ...config.webp_options}))
    .pipe(size({ showFiles: true, showTotal: false }))
    .pipe(gulp.dest(config.paths.dist));

  const jpegsToWebp = gulp
    .src(config.paths.images + "**/*.{jpg,jpeg}")
    .pipe(plumber())
    .pipe(webp({lessless: false, ...config.webp_options}))
    .pipe(size({ showFiles: true, showTotal: false }))
    .pipe(gulp.dest(config.paths.dist));

  return merge(pngs, jpegs, pngsToWebp, jpegsToWebp);
}

gulp.task("imagemin", minifyImages);
