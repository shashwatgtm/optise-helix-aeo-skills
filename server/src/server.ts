import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import { ListToolsRequestSchema, CallToolRequestSchema } from '@modelcontextprotocol/sdk/types.js';
import { waveTools, callWaveTool } from './wave2-checkers.js';
export function createServer(){const server=new Server({name:'optise-helix-aeo-skills-candidate',version:'1.5.0'},{capabilities:{tools:{}}});server.setRequestHandler(ListToolsRequestSchema,async()=>({tools:waveTools}));server.setRequestHandler(CallToolRequestSchema,async r=>callWaveTool(r.params.name,r.params.arguments));return server;}
