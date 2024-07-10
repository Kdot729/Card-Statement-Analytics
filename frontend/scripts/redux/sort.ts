import { createSlice } from '@reduxjs/toolkit'
import type { PayloadAction } from '@reduxjs/toolkit'

const initialState = {value: "Unsorted"}

export const Sort_Slice = createSlice(
{
    
    name: 'Sort',
    initialState,
    reducers:   {
                    Unsorted: (state, action) => {},
                    Sorted: (state, action) => {Sort_Table(action.payload)}
                },
})

const Sort_Table = (ID) => 
{
    const Split_ID: string = ID.split("-");
    const Column: string = Split_ID[0]
    const Sort_Direction: string = Split_ID[1].toLocaleLowerCase()
}

export const { Sorted, Unsorted } = Sort_Slice.actions

export default Sort_Slice.reducer