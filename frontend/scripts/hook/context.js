import { createContext, useContext } from 'react';

export const Create_Context = createContext("")

export const Use_Context = (PDF_ID) => {return useContext(PDF_ID)}