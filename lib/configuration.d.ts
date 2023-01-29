import type { Static } from '@feathersjs/typebox';
export declare const configurationSchema: import("@sinclair/typebox").TIntersect<[import("@sinclair/typebox").TObject<{
    authentication: import("@sinclair/typebox").TOptional<import("@sinclair/typebox").TObject<{
        secret: import("@sinclair/typebox").TString<string>;
        entity: import("@sinclair/typebox").TOptional<import("@sinclair/typebox").TString<string>>;
        entityId: import("@sinclair/typebox").TOptional<import("@sinclair/typebox").TString<string>>;
        service: import("@sinclair/typebox").TOptional<import("@sinclair/typebox").TString<string>>;
        authStrategies: import("@sinclair/typebox").TArray<import("@sinclair/typebox").TString<string>>;
        parseStrategies: import("@sinclair/typebox").TOptional<import("@sinclair/typebox").TArray<import("@sinclair/typebox").TString<string>>>;
        jwtOptions: import("@sinclair/typebox").TOptional<import("@sinclair/typebox").TObject<{}>>;
        jwt: import("@sinclair/typebox").TOptional<import("@sinclair/typebox").TObject<{
            header: import("@sinclair/typebox").TString<string>;
            schemes: import("@sinclair/typebox").TString<string>;
        }>>;
        local: import("@sinclair/typebox").TOptional<import("@sinclair/typebox").TObject<{
            usernameField: import("@sinclair/typebox").TString<string>;
            passwordField: import("@sinclair/typebox").TString<string>;
            hashSize: import("@sinclair/typebox").TOptional<import("@sinclair/typebox").TNumber>;
            errorMessage: import("@sinclair/typebox").TOptional<import("@sinclair/typebox").TString<string>>;
            entityUsernameField: import("@sinclair/typebox").TOptional<import("@sinclair/typebox").TString<string>>;
            entityPasswordField: import("@sinclair/typebox").TOptional<import("@sinclair/typebox").TString<string>>;
        }>>;
        oauth: import("@sinclair/typebox").TOptional<import("@sinclair/typebox").TObject<{
            redirect: import("@sinclair/typebox").TOptional<import("@sinclair/typebox").TString<string>>;
            origins: import("@sinclair/typebox").TOptional<import("@sinclair/typebox").TArray<import("@sinclair/typebox").TString<string>>>;
            defaults: import("@sinclair/typebox").TOptional<import("@sinclair/typebox").TObject<{
                key: import("@sinclair/typebox").TOptional<import("@sinclair/typebox").TString<string>>;
                secret: import("@sinclair/typebox").TOptional<import("@sinclair/typebox").TString<string>>;
            }>>;
        }>>;
    }>>;
    paginate: import("@sinclair/typebox").TOptional<import("@sinclair/typebox").TObject<{
        default: import("@sinclair/typebox").TNumber;
        max: import("@sinclair/typebox").TNumber;
    }>>;
    origins: import("@sinclair/typebox").TOptional<import("@sinclair/typebox").TArray<import("@sinclair/typebox").TString<string>>>;
    mongodb: import("@sinclair/typebox").TOptional<import("@sinclair/typebox").TString<string>>;
    mysql: import("@sinclair/typebox").TOptional<import("@sinclair/typebox").TObject<{
        client: import("@sinclair/typebox").TString<string>;
        connection: import("@sinclair/typebox").TString<string>;
    }>>;
    postgresql: import("@sinclair/typebox").TOptional<import("@sinclair/typebox").TObject<{
        client: import("@sinclair/typebox").TString<string>;
        connection: import("@sinclair/typebox").TString<string>;
    }>>;
    sqlite: import("@sinclair/typebox").TOptional<import("@sinclair/typebox").TObject<{
        client: import("@sinclair/typebox").TString<string>;
        connection: import("@sinclair/typebox").TString<string>;
    }>>;
    mssql: import("@sinclair/typebox").TOptional<import("@sinclair/typebox").TObject<{
        client: import("@sinclair/typebox").TString<string>;
        connection: import("@sinclair/typebox").TString<string>;
    }>>;
}>, import("@sinclair/typebox").TObject<{
    host: import("@sinclair/typebox").TString<string>;
    port: import("@sinclair/typebox").TNumber;
    public: import("@sinclair/typebox").TString<string>;
}>]>;
export type ApplicationConfiguration = Static<typeof configurationSchema>;
export declare const configurationValidator: import("@feathersjs/schema/lib").Validator<any, any>;
