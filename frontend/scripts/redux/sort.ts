import { createSlice } from '@reduxjs/toolkit'
import type { PayloadAction } from '@reduxjs/toolkit'

const initialState = {value: "Unsorted"}

export const Sort_Slice = createSlice(
{
    
    name: 'Sort',
    initialState,
    reducers:   {
                    Ascending: (state, action) => {},
                    Descending: (state, action) => {},
                    Unsorted: (state) => {},
                },
})

export const { Ascending, Descending, Unsorted } = Sort_Slice.actions

export default Sort_Slice.reducer