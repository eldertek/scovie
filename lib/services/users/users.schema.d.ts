import type { Static } from '@feathersjs/typebox';
import type { HookContext } from '../../declarations';
export declare const userSchema: import("@sinclair/typebox").TObject<{
    id: import("@sinclair/typebox").TNumber;
    email: import("@sinclair/typebox").TString<string>;
    password: import("@sinclair/typebox").TOptional<import("@sinclair/typebox").TString<string>>;
}>;
export type User = Static<typeof userSchema>;
export declare const userResolver: import("@feathersjs/schema").Resolver<{
    password?: string | undefined;
    id: number;
    email: string;
}, HookContext<any>>;
export declare const userExternalResolver: import("@feathersjs/schema").Resolver<{
    password?: string | undefined;
    id: number;
    email: string;
}, HookContext<any>>;
export declare const userDataSchema: import("@sinclair/typebox").TPick<import("@sinclair/typebox").TObject<{
    id: import("@sinclair/typebox").TNumber;
    email: import("@sinclair/typebox").TString<string>;
    password: import("@sinclair/typebox").TOptional<import("@sinclair/typebox").TString<string>>;
}>, ["email", "password"]>;
export type UserData = Static<typeof userDataSchema>;
export declare const userDataValidator: import("@feathersjs/schema").DataValidatorMap;
export declare const userDataResolver: import("@feathersjs/schema").Resolver<{
    password?: string | undefined;
    id: number;
    email: string;
}, HookContext<any>>;
export declare const userPatchSchema: import("@sinclair/typebox").TPartial<import("@sinclair/typebox").TObject<{
    id: import("@sinclair/typebox").TNumber;
    email: import("@sinclair/typebox").TString<string>;
    password: import("@sinclair/typebox").TOptional<import("@sinclair/typebox").TString<string>>;
}>>;
export type UserPatch = Static<typeof userPatchSchema>;
export declare const userPatchValidator: import("@feathersjs/schema").DataValidatorMap;
export declare const userPatchResolver: import("@feathersjs/schema").Resolver<{
    password?: string | undefined;
    id: number;
    email: string;
}, HookContext<any>>;
export declare const userQueryProperties: import("@sinclair/typebox").TPick<import("@sinclair/typebox").TObject<{
    id: import("@sinclair/typebox").TNumber;
    email: import("@sinclair/typebox").TString<string>;
    password: import("@sinclair/typebox").TOptional<import("@sinclair/typebox").TString<string>>;
}>, ["id", "email"]>;
export declare const userQuerySchema: import("@sinclair/typebox").TIntersect<[import("@sinclair/typebox").TIntersect<[import("@sinclair/typebox").TPartial<import("@sinclair/typebox").TObject<{
    $limit: import("@sinclair/typebox").TNumber;
    $skip: import("@sinclair/typebox").TNumber;
    $sort: import("@sinclair/typebox").TObject<{
        id: import("@sinclair/typebox").TOptional<import("@sinclair/typebox").TInteger>;
        email: import("@sinclair/typebox").TOptional<import("@sinclair/typebox").TInteger>;
    }>;
    $select: import("@sinclair/typebox").TUnsafe<("id" | "email")[]>;
    $or: import("@sinclair/typebox").TArray<import("@sinclair/typebox").TOptional<import("@sinclair/typebox").TObject<{
        id: import("@sinclair/typebox").TOptional<import("@sinclair/typebox").TUnion<[import("@sinclair/typebox").TNumber, import("@sinclair/typebox").TPartial<import("@sinclair/typebox").TObject<{
            $gt: import("@sinclair/typebox").TNumber;
            $gte: import("@sinclair/typebox").TNumber;
            $lt: import("@sinclair/typebox").TNumber;
            $lte: import("@sinclair/typebox").TNumber;
            $ne: import("@sinclair/typebox").TNumber;
            $in: import("@sinclair/typebox").TArray<import("@sinclair/typebox").TNumber>;
            $nin: import("@sinclair/typebox").TArray<import("@sinclair/typebox").TNumber>;
        } & {
            [key: string]: import("@sinclair/typebox").TSchema;
        }>>]>>;
        email: import("@sinclair/typebox").TOptional<import("@sinclair/typebox").TUnion<[import("@sinclair/typebox").TString<string>, import("@sinclair/typebox").TPartial<import("@sinclair/typebox").TObject<{
            $gt: import("@sinclair/typebox").TString<string>;
            $gte: import("@sinclair/typebox").TString<string>;
            $lt: import("@sinclair/typebox").TString<string>;
            $lte: import("@sinclair/typebox").TString<string>;
            $ne: import("@sinclair/typebox").TString<string>;
            $in: import("@sinclair/typebox").TArray<import("@sinclair/typebox").TString<string>>;
            $nin: import("@sinclair/typebox").TArray<import("@sinclair/typebox").TString<string>>;
        } & {
            [key: string]: import("@sinclair/typebox").TSchema;
        }>>]>>;
    }>>>;
    $and: import("@sinclair/typebox").TArray<import("@sinclair/typebox").TOptional<import("@sinclair/typebox").TObject<{
        id: import("@sinclair/typebox").TOptional<import("@sinclair/typebox").TUnion<[import("@sinclair/typebox").TNumber, import("@sinclair/typebox").TPartial<import("@sinclair/typebox").TObject<{
            $gt: import("@sinclair/typebox").TNumber;
            $gte: import("@sinclair/typebox").TNumber;
            $lt: import("@sinclair/typebox").TNumber;
            $lte: import("@sinclair/typebox").TNumber;
            $ne: import("@sinclair/typebox").TNumber;
            $in: import("@sinclair/typebox").TArray<import("@sinclair/typebox").TNumber>;
            $nin: import("@sinclair/typebox").TArray<import("@sinclair/typebox").TNumber>;
        } & {
            [key: string]: import("@sinclair/typebox").TSchema;
        }>>]>>;
        email: import("@sinclair/typebox").TOptional<import("@sinclair/typebox").TUnion<[import("@sinclair/typebox").TString<string>, import("@sinclair/typebox").TPartial<import("@sinclair/typebox").TObject<{
            $gt: import("@sinclair/typebox").TString<string>;
            $gte: import("@sinclair/typebox").TString<string>;
            $lt: import("@sinclair/typebox").TString<string>;
            $lte: import("@sinclair/typebox").TString<string>;
            $ne: import("@sinclair/typebox").TString<string>;
            $in: import("@sinclair/typebox").TArray<import("@sinclair/typebox").TString<string>>;
            $nin: import("@sinclair/typebox").TArray<import("@sinclair/typebox").TString<string>>;
        } & {
            [key: string]: import("@sinclair/typebox").TSchema;
        }>>]>>;
    }>>>;
}>>, import("@sinclair/typebox").TOptional<import("@sinclair/typebox").TObject<{
    id: import("@sinclair/typebox").TOptional<import("@sinclair/typebox").TUnion<[import("@sinclair/typebox").TNumber, import("@sinclair/typebox").TPartial<import("@sinclair/typebox").TObject<{
        $gt: import("@sinclair/typebox").TNumber;
        $gte: import("@sinclair/typebox").TNumber;
        $lt: import("@sinclair/typebox").TNumber;
        $lte: import("@sinclair/typebox").TNumber;
        $ne: import("@sinclair/typebox").TNumber;
        $in: import("@sinclair/typebox").TArray<import("@sinclair/typebox").TNumber>;
        $nin: import("@sinclair/typebox").TArray<import("@sinclair/typebox").TNumber>;
    } & {
        [key: string]: import("@sinclair/typebox").TSchema;
    }>>]>>;
    email: import("@sinclair/typebox").TOptional<import("@sinclair/typebox").TUnion<[import("@sinclair/typebox").TString<string>, import("@sinclair/typebox").TPartial<import("@sinclair/typebox").TObject<{
        $gt: import("@sinclair/typebox").TString<string>;
        $gte: import("@sinclair/typebox").TString<string>;
        $lt: import("@sinclair/typebox").TString<string>;
        $lte: import("@sinclair/typebox").TString<string>;
        $ne: import("@sinclair/typebox").TString<string>;
        $in: import("@sinclair/typebox").TArray<import("@sinclair/typebox").TString<string>>;
        $nin: import("@sinclair/typebox").TArray<import("@sinclair/typebox").TString<string>>;
    } & {
        [key: string]: import("@sinclair/typebox").TSchema;
    }>>]>>;
}>>]>, import("@sinclair/typebox").TObject<{}>]>;
export type UserQuery = Static<typeof userQuerySchema>;
export declare const userQueryValidator: import("@feathersjs/schema").Validator<any, any>;
export declare const userQueryResolver: import("@feathersjs/schema").Resolver<Partial<{
    $limit: number;
    $skip: number;
    $sort: {
        id?: number | undefined;
        email?: number | undefined;
    };
    $select: ("id" | "email")[];
    $or: {
        id?: number | Partial<{
            [x: string]: unknown;
            [x: number]: unknown;
        }> | undefined;
        email?: string | Partial<{
            [x: string]: unknown;
            [x: number]: unknown;
        }> | undefined;
    }[];
    $and: {
        id?: number | Partial<{
            [x: string]: unknown;
            [x: number]: unknown;
        }> | undefined;
        email?: string | Partial<{
            [x: string]: unknown;
            [x: number]: unknown;
        }> | undefined;
    }[];
}> & {
    id?: number | Partial<{
        [x: string]: unknown;
        [x: number]: unknown;
    }> | undefined;
    email?: string | Partial<{
        [x: string]: unknown;
        [x: number]: unknown;
    }> | undefined;
} & {}, HookContext<any>>;
