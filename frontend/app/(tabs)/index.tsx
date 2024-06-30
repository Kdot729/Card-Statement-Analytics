
import React from 'react';
import File from '../components/file';
import { QueryClient, QueryClientProvider } from 'react-query';

const Query_Client = new QueryClient();

export default function App() 
{

    return  (
            <QueryClientProvider client={Query_Client}>
                <File />
            </QueryClientProvider>
            )
}