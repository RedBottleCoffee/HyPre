import { Hypre } from "./dist/js/libs/hypre";
import { Pyproc } from './dist/js/libs/pyproc'
const hyper = new Hypre();
// hyper.exit();

var pyproc = new Pyproc('printman.py')
pyproc.asyncRun((data) => {

})
