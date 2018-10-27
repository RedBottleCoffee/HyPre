var gulp = require('gulp');
var sass = require('gulp-sass');
var sassGlob = require("gulp-sass-glob");
var babel = require("gulp-babel");
var electron = require('electron-connect').server.create();

var srcDir = './app/src';
var distDir = './app/dist';

gulp.task('start', ['compile'], function() {
  electron.start('./app');

  gulp.watch([srcDir + '/js/**/*.js'], ['compile']);
  gulp.watch(['./app/index.js'], electron.restart);
  gulp.watch(['./app/src/scss/*.scss'], ['sass']);
  gulp.watch(['./app/dist/*.css'], electron.reload);
  gulp.watch(['./app/*.html'], electron.reload);
});

gulp.task('compile', function(){
  return gulp.src(srcDir + '/js/**/*.{js,jsx}')
    .pipe(babel())
    .pipe(gulp.dest(distDir + '/js'));
});

gulp.task('sass', function(){
  gulp.src('./app/src/scss/style.scss')
    .pipe(sassGlob())
    .pipe(sass())
    .pipe(gulp.dest('./app/dist/'));
});
