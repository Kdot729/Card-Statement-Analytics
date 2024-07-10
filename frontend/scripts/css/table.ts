import {StyleSheet} from 'react-native';

export const Table_Element = (Background_Color) =>
{
    return StyleSheet.create({Element: {flexDirection: "row", backgroundColor: Background_Color}})["Element"]
}