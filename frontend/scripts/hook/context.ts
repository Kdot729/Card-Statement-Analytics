import { Context, createContext, useContext } from 'react';

export const Create_Context: Context<string> = createContext("")

export const Use_Context = (PDF_ID: Context<string>) => {return useContext(PDF_ID)}