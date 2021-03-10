var gulp = require('gulp');
var path = require('path');
var sass = require('gulp-sass');
var autoprefixer = require('gulp-autoprefixer');
var sourcemaps = require('gulp-sourcemaps');
var open = require('gulp-open');
var browserSync = require('browser-sync').create();
var wait = require('gulp-wait');

var Paths = {
  HERE: './',
  DIST: 'dist/',
  CSS1: './task_manager/static/css/',
  CSS2: './task_manager/static/css/landing.css',
  SCSS_TOOLKIT_SOURCES1: './task_manager/static/assets/scss/black-dashboard.scss',
  SCSS_TOOLKIT_SOURCES2: './src/scss/**/**',
  SCSS: './task_manager/static/assets/scss/**/**',
};

gulp.task('browserSync', function () {
  browserSync.init({
    notify: false,
    port: 8000,
    proxy: 'localhost:8000'
  });
});

// Compile SCSS
gulp.task('scss1', function () {
  return gulp.src(Paths.SCSS_TOOLKIT_SOURCES1)
    // .pipe(wait(500))
    .pipe(sourcemaps.init())
    .pipe(sass().on('error', sass.logError))
    .pipe(autoprefixer({
      overrideBrowserslist: ['> 1%']
    }))
    .pipe(sourcemaps.write('.'))
    .pipe(gulp.dest(Paths.CSS1))
    .pipe(browserSync.stream());
});

gulp.task('scss2', function () {
  return gulp.src(Paths.SCSS_TOOLKIT_SOURCES2, Paths.CSS )
    .pipe(sourcemaps.init())
    .pipe(sass().on('error', sass.logError))
    .pipe(autoprefixer({
      overrideBrowserslist: ['> 1%']
    }))
    .pipe(sourcemaps.write('.'))
    .pipe(gulp.dest(Paths.CSS2))
    .pipe(browserSync.stream());
});

gulp.task('serve', gulp.series('scss1', 'scss2', function () {
  browserSync.init({
      // server: paths.temp.base
      port: 8000,
      proxy: 'localhost:8000'
  });

  gulp.watch([Paths.SCSS_TOOLKIT_SOURCES2 + '/**/*.scss', Paths.SCSS_TOOLKIT_SOURCES2 + '/**/*.scss'], gulp.series('scss1', 'scss2'));
}));


// gulp.task('watch', function () {
//   gulp.watch(Paths.SCSS, ['scss']);
// });

gulp.task('build', gulp.series('scss1', 'scss2'));
gulp.task('default', gulp.series('scss1', 'scss2', 'serve'));