import type { Knex } from 'knex';
import type { Application } from './declarations';
declare module './declarations' {
    interface Configuration {
        sqliteClient: Knex;
    }
}
export declare const sqlite: (app: Application) => void;
