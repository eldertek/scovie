"use strict";
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    var desc = Object.getOwnPropertyDescriptor(m, k);
    if (!desc || ("get" in desc ? !m.__esModule : desc.writable || desc.configurable)) {
      desc = { enumerable: true, get: function() { return m[k]; } };
    }
    Object.defineProperty(o, k2, desc);
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __exportStar = (this && this.__exportStar) || function(m, exports) {
    for (var p in m) if (p !== "default" && !Object.prototype.hasOwnProperty.call(exports, p)) __createBinding(exports, m, p);
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.user = void 0;
// For more information about this file see https://dove.feathersjs.com/guides/cli/service.html
const authentication_1 = require("@feathersjs/authentication");
const schema_1 = require("@feathersjs/schema");
const users_schema_1 = require("./users.schema");
const users_class_1 = require("./users.class");
__exportStar(require("./users.class"), exports);
__exportStar(require("./users.schema"), exports);
// A configure function that registers the service and its hooks via `app.configure`
const user = (app) => {
    // Register our service on the Feathers application
    app.use('users', new users_class_1.UserService((0, users_class_1.getOptions)(app)), {
        // A list of all methods this service exposes externally
        methods: ['find', 'get', 'create', 'patch', 'remove'],
        // You can add additional custom events to be sent to clients here
        events: []
    });
    // Initialize hooks
    app.service('users').hooks({
        around: {
            all: [schema_1.hooks.resolveExternal(users_schema_1.userExternalResolver), schema_1.hooks.resolveResult(users_schema_1.userResolver)],
            find: [(0, authentication_1.authenticate)('jwt')],
            get: [(0, authentication_1.authenticate)('jwt')],
            create: [],
            update: [(0, authentication_1.authenticate)('jwt')],
            patch: [(0, authentication_1.authenticate)('jwt')],
            remove: [(0, authentication_1.authenticate)('jwt')]
        },
        before: {
            all: [schema_1.hooks.validateQuery(users_schema_1.userQueryValidator), schema_1.hooks.resolveQuery(users_schema_1.userQueryResolver)],
            find: [],
            get: [],
            create: [schema_1.hooks.validateData(users_schema_1.userDataValidator), schema_1.hooks.resolveData(users_schema_1.userDataResolver)],
            patch: [schema_1.hooks.validateData(users_schema_1.userPatchValidator), schema_1.hooks.resolveData(users_schema_1.userPatchResolver)],
            remove: []
        },
        after: {
            all: []
        },
        error: {
            all: []
        }
    });
};
exports.user = user;
