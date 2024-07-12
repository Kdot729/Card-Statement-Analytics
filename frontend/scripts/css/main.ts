import {StyleSheet} from 'react-native';

const CSS = StyleSheet.create(
{
    Center: {justifyContent: "center", alignItems: "center"}
})

export const Center = CSS["Center"]

export const Font_Size = (Size: number) =>
{
    return StyleSheet.create({Font_Size: {fontSize: Size}})["Font_Size"]
}

export const Margin = (Margin_Number: number) =>
{
    return StyleSheet.create({Margin: {margin: Margin_Number}})["Margin"]
}

export const Flex = (Flex_Number: number) =>
{
    return StyleSheet.create({Flex: {flex: Flex_Number}})["Flex"]
}