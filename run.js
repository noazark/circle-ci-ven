const assert = require('assert');

const expected = '6.5.0';
const version = process.version;

assert(version.indexOf(expected) >= 0, 'expected python version to be ' + version + ', but is actually ' + expected);
