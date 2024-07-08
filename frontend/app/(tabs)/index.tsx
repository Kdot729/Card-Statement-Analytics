
import React from 'react';
import File from '../components/file';
import { QueryClient, QueryClientProvider } from 'react-query';
import { store } from '@/scripts/redux/store';
import { Provider } from 'react-redux'

const Query_Client = new QueryClient();

export default function App() 
{

    return  (
            <QueryClientProvider client={Query_Client}>
                <Provider store={store}>
                <File />
                </Provider>
            </QueryClientProvider>
            )
}