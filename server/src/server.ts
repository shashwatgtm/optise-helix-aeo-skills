import {reserveTools,isReserveTool,callReserveTool} from './reserve-tools.js';
import {attachWidgets} from './widget-layer.js';
import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import { ListToolsRequestSchema, CallToolRequestSchema } from '@modelcontextprotocol/sdk/types.js';
import { waveTools, callWaveTool } from './wave2-checkers.js';
export function createServer(){const server=new Server({name:'optise-helix-aeo-skills-candidate',version:'1.5.0'},{capabilities:{tools:{}}});attachWidgets(server);server.setRequestHandler(ListToolsRequestSchema,async()=>({tools:[...waveTools,...reserveTools()]}));server.setRequestHandler(CallToolRequestSchema,async r=>isReserveTool(r.params.name)?callReserveTool(r.params.name,r.params.arguments):callWaveTool(r.params.name,r.params.arguments));return server;}
