import { AuthenticationService } from '@feathersjs/authentication';
import type { Application } from './declarations';
declare module './declarations' {
    interface ServiceTypes {
        authentication: AuthenticationService;
    }
}
export declare const authentication: (app: Application) => void;
