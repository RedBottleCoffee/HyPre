import { spawn } from "child_process";

export class Pyproc {
  constructor(path='./pyproc/predictor.py') {
    self.path = path
  }

  async asyncRun(callback) {
    const process = spawn('python', [self.path])
    process.stdout.on('data', callback)
  }
}
