import { HookContext as FeathersHookContext, NextFunction } from '@feathersjs/feathers';
import { Application as FeathersApplication } from '@feathersjs/koa';
import { ApplicationConfiguration } from './configuration';
import { User } from './services/users/users';
export { NextFunction };
export interface Configuration extends ApplicationConfiguration {
}
export interface ServiceTypes {
}
export type Application = FeathersApplication<ServiceTypes, Configuration>;
export type HookContext<S = any> = FeathersHookContext<Application, S>;
declare module '@feathersjs/feathers' {
    interface Params {
        user?: User;
    }
}
