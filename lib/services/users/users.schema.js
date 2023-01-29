"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.userQueryResolver = exports.userQueryValidator = exports.userQuerySchema = exports.userQueryProperties = exports.userPatchResolver = exports.userPatchValidator = exports.userPatchSchema = exports.userDataResolver = exports.userDataValidator = exports.userDataSchema = exports.userExternalResolver = exports.userResolver = exports.userSchema = void 0;
// For more information about this file see https://dove.feathersjs.com/guides/cli/service.schemas.html
const schema_1 = require("@feathersjs/schema");
const typebox_1 = require("@feathersjs/typebox");
const authentication_local_1 = require("@feathersjs/authentication-local");
const validators_1 = require("../../validators");
// Main data model schema
exports.userSchema = typebox_1.Type.Object({
    id: typebox_1.Type.Number(),
    email: typebox_1.Type.String(),
    password: typebox_1.Type.Optional(typebox_1.Type.String())
}, { $id: 'User', additionalProperties: false });
exports.userResolver = (0, schema_1.resolve)({});
exports.userExternalResolver = (0, schema_1.resolve)({
    // The password should never be visible externally
    password: async () => undefined
});
// Schema for creating new users
exports.userDataSchema = typebox_1.Type.Pick(exports.userSchema, ['email', 'password'], {
    $id: 'UserData',
    additionalProperties: false
});
exports.userDataValidator = (0, typebox_1.getDataValidator)(exports.userDataSchema, validators_1.dataValidator);
exports.userDataResolver = (0, schema_1.resolve)({
    password: (0, authentication_local_1.passwordHash)({ strategy: 'local' })
});
// Schema for updating existing users
exports.userPatchSchema = typebox_1.Type.Partial(exports.userSchema, {
    $id: 'UserPatch'
});
exports.userPatchValidator = (0, typebox_1.getDataValidator)(exports.userPatchSchema, validators_1.dataValidator);
exports.userPatchResolver = (0, schema_1.resolve)({
    password: (0, authentication_local_1.passwordHash)({ strategy: 'local' })
});
// Schema for allowed query properties
exports.userQueryProperties = typebox_1.Type.Pick(exports.userSchema, ['id', 'email']);
exports.userQuerySchema = typebox_1.Type.Intersect([
    (0, typebox_1.querySyntax)(exports.userQueryProperties),
    // Add additional query properties here
    typebox_1.Type.Object({}, { additionalProperties: false })
], { additionalProperties: false });
exports.userQueryValidator = (0, typebox_1.getValidator)(exports.userQuerySchema, validators_1.queryValidator);
exports.userQueryResolver = (0, schema_1.resolve)({
    // If there is a user (e.g. with authentication), they are only allowed to see their own data
    id: async (value, user, context) => {
        if (context.params.user) {
            return context.params.user.id;
        }
        return value;
    }
});
