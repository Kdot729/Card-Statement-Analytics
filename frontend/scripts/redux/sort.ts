import { createSlice } from '@reduxjs/toolkit'
import type { PayloadAction } from '@reduxjs/toolkit'

const initialState = {URL: "get/PDF"}

export const Sort_Slice = createSlice(
{
    
    name: 'Sort',
    initialState,
    reducers:   {
                    Unsorted: (state, action) => {},
                    Sorted: (state, action) => 
                    {
                        state.URL = Sorted_URL(action.payload)
                    }
                },
})

const Sorted_URL = (ID) => 
{
    const Split_ID: string = ID.split("-");
    const Column: string = Split_ID[0]
    const Sort_Direction: string = Split_ID[1].toLocaleLowerCase()

    return `get/${Sort_Direction}/${Column}/PDF`
}

export const { Sorted, Unsorted } = Sort_Slice.actions

export default Sort_Slice.reducer