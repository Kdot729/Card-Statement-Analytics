import { configureStore } from '@reduxjs/toolkit'
import Sorting_Reducer  from './sort'

export const store = configureStore(
{
    reducer: {Sorting: Sorting_Reducer},
})

// Infer the `RootState` and `AppDispatch` types from the store itself
export type RootState = ReturnType<typeof store.getState>

// Inferred type: {posts: PostsState, comments: CommentsState, users: UsersState}
export type AppDispatch = typeof store.dispatch